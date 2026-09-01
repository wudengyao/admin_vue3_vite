// 生产环境 mock 服务：通过 mockjs 在浏览器端拦截 XHR 请求
import { createProdMockServer } from "vite-plugin-mock/es/createProdMockServer";
import indexMock from "./mock/index";

export function setupProdMockServer() {
	createProdMockServer([...indexMock]);
}
