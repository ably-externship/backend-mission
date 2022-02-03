import axios from 'axios';

const client = axios.create();

client.interceptors.request.use(
  function (config) {
    // 요청을 보내기 전에 수행할 일
    // token 설정
    config.headers['Authorization'] = `Bearer ${sessionStorage.getItem('Access-Token')}`

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
  error => {
    // 오류 응답을 처리
    // ...##
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
