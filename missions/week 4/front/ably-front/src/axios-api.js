import axios from 'axios';
import jwt_decode from "jwt-decode";


const client = axios.create();

client.interceptors.request.use(

  function (config) {
    // 요청을 보내기 전에 수행할 일
    // token 설정
    const token = sessionStorage.getItem('Access-Token');
    
    config.headers['Authorization'] = `Bearer ${token}`
    return config;
    

    
  },
  function (error) {
    // 오류 요청을 보내기전 수행할 일
    // ...
    return Promise.reject(error);
  },
);


client.interceptors.response.use(
  response => {
    // 응답 데이터를 가공
    // ...
    return response;
  },
  async(error) => {
    const { config, response: {status}} = error;

    const originalRequest = config;

    if ( status === 401 ) {
      const refreshClient = axios.create();
      refreshClient.get('http://127.0.0.1:8000/auth/refresh',{withCredentials: true}).then(response => {
          const data = response.data;
          const accessToken = data.data;
          sessionStorage.setItem('Access-Token', accessToken);
          config.headers['Authorization'] = `Bearer ${accessToken}`

          originalRequest.headers = {
            'Authorization': `Bearer ${accessToken}`
          }
          return axios(originalRequest);          
      }).catch(error => {
          console.log(error)
      })
    }
    return Promise.reject(error);
  },
);

export const callApi = async (type, url, params, options) => {
  try {
    const upperType = type.toUpperCase();
    let response = '';

    if (upperType === 'GET') {
      response = await client.get(url, { ...options, params: params });
    } else if (upperType === 'POST') {
      response = await client.post(url, params, options);
    } else if (upperType === 'PUT') {
      response = await client.put(url, params, options);
    } else if (upperType === 'DELETE') {
      response = await client.delete(url, { ...options, data: params });
    }

    return response;
  } catch (error) {
    throw error;
  }
};
