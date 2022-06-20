import Vue from 'vue'
import Router from 'vue-router'
import Welcome from './views/Welcome.vue'
import Home from './views/Home'
import ProjectList from "@/views/ProjectList";
// 定义vue插件
Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            // elementCreate 元素生成,懒加载
            // #t 访问时渲染 懒加载
            component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
        },
        {
            path: '/welcome',
            name: 'welcome',
            component: Welcome
        },
        {
            path: '/project_list',
            name: 'project_list',
            component: ProjectList
        }
    ]
})
