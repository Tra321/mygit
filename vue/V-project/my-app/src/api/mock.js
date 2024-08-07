import Mockjs from "mockjs";
import homeApi from './mockServeData/home'

// 定义mock请求拦截
Mockjs.mock('/api/home/getData', homeApi.getStatisticalData)