import axios, {AxiosInstance, AxiosResponse} from "axios";

const client: AxiosInstance = axios.create({
    baseURL: process.env.NODE_ENV === 'development' ? '/' : 'https://mbly.o-r.cc',
    withCredentials: true
});

export interface TokenResponse {
    access: string;
    refresh?: string;
}

export const token = (username: string, password: string): Promise<AxiosResponse<TokenResponse>> => client.post('/apis/accounts/token/', {
    username, password
});
export const refreshToken = (refresh: string): Promise<AxiosResponse<TokenResponse>> => client.post('/apis/accounts/token/refresh/', {refresh});

export function setBearer(access: string) {
    if (client != null) {
        client.defaults.headers.common['Authorization'] = `Bearer ${access}`;
    }
}

export interface ProductRequest {
    name: string;
    display_name: string;
    original_price: number;
    discounted_price: number;
    detail: string;
    hidden: boolean;
    sold_out: boolean;
    category: number;
}

export interface ProductResponse extends ProductRequest {
    id: number;
    market: number;
    review_count: number;
    review_point: number;
    created_at: string;
    updated_at: string;
}

export const findAllProducts = (): Promise<AxiosResponse<Array<ProductResponse>>> => client.get('/apis/products/');
export const findProductById = (id: number): Promise<AxiosResponse<ProductResponse>> => client.get(`/apis/products/${id}/`);
export const addProduct = (requestBody: ProductRequest) => client.post('/apis/products/');
export const editProduct = (id: number, requestBody: ProductRequest) => client.put(`/apis/products/${id}/`, requestBody);
export const removeProduct = (id: number) => client.delete(`/apis/products/${id}/`);

export const searchProducts = (query: string): Promise<AxiosResponse<Array<ProductResponse>>> => client.get(`/apis/products/?search=${query}`);

export interface ProductOptionRequest {
    option1_type: string;
    option1_name: string;
    option1_display_name: string;
    option2_type: string;
    option2_name: string;
    option2_display_name: string;
    option3_type: string;
    option3_name: string;
    option3_display_name: string;
    hidden: boolean;
    sold_out: boolean;
    added_price: number;
    stock: number;
}

export interface ProductOptionResponse extends ProductOptionRequest {
    id: number;
    product: number;
    created_at: string;
    updated_at: string;
}

export const findAllProductOptions = (productId: number): Promise<AxiosResponse<Array<ProductOptionResponse>>> => client.get(`/apis/products/${productId}/options/`);
export const findProductOptionById = (productId: number, id: number): Promise<AxiosResponse<ProductOptionResponse>> => client.get(`/apis/products/${productId}/options/${id}/`);
export const addProductOption = (productId: number, requestBody: ProductOptionRequest) => client.post(`/apis/products/${productId}/options/`, requestBody);
export const editProductOption = (productId: number, id: number, requestBody: ProductOptionRequest) => client.post(`/apis/products/${productId}/options/${id}/`, requestBody);
export const removeProductOption = (productId: number, id: number) => client.post(`/apis/products/${productId}/options/${id}/`);

export default client;
