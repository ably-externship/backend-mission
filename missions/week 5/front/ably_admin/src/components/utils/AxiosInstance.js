import axios from 'axios'

const baseURL = 'http://localhost:8000/api'


let accessToken = localStorage.getItem("ACCESS_TOKEN")

// 토큰의 페이로드 부분에서 만료시간 가져오기
function getPayloadFromJWTExp(token) {
    const base64Payload = atob(token.split(".")[1]);
    return base64Payload.split('"exp":')[1].split(',"')[0];
}


// 어떠한 시각이 현재로 부터 몇초 남았는지
function secondsDiffFromNow(exp) {
    const diffMillis = parseInt(exp + "000") - new Date().getTime();
    return parseInt(diffMillis / 1000);
}


const axiosInstance = axios.create({
    baseURL,
    headers: {
        Authorization: `Bearer ${accessToken}`
    }
})



axiosInstance.interceptors.request.use(
    async req => {
        if (! accessToken){
            accessToken  = localStorage.getItem("ACCESS_TOKEN")
            req.headers.Authorization = `Bearer ${accessToken}`
        }

        let exptime = getPayloadFromJWTExp(accessToken)
        // 만료
        let remainexpired = secondsDiffFromNow(exptime) 
        console.log(remainexpired)
        let isexpired = remainexpired< 1
        
        // access token 재발급
        if (isexpired){
            await axios.post(`${baseURL}/account/token/refresh`,{
                refresh:localStorage.getItem("REFRESH_TOKEN")
            })
            .then(response =>  {
                localStorage.setItem("ACCESS_TOKEN",response.data.access)
            })
            req.headers.Authorization = `Bearer ${accessToken}`
            return req
        }
        return req
    })

export default axiosInstance;