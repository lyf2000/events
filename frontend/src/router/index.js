import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    }, {
        path: '/signup',
        props: true,
        name: 'SignUp',
        component: () => import('../views/SignUp')
    }, {
        path: '/login',
        props: true,
        name: 'SignIn',
        component: () => import('../views/SignIn')
    },

    // {
    //     path: '/about',
    //     name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: function () {
    //     return import(/* webpackChunkName: "about" */ '../views/About.vue')
    // }
    // }
];
const router = new VueRouter({
    mode: 'history',
    routes
})

export default router
