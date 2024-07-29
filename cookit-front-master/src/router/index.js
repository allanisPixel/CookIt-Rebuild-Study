import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../components/Index.vue'
import PaginaReceita from '../components/receitas/PaginaReceita'
import FormReceita from '../components/receitas/FormReceita'
import EditarPerfil from '../components/usuario/EditarPerfil'
import LoginCadastro from '../components/usuario/LoginCadastro'
import EditarReceita from '../components/receitas/EditarReceita'
import Login from '../components/usuario/Login'
import Cadastro from '../components/usuario/Cadastro'
import Perfil from '../components/usuario/Perfil'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Index',
        component: Index
    },
    {
        path: '/FormReceita/',
        name: 'FormReceita',
        component: FormReceita
    },
    {
        path: '/PaginaReceita/:id', 
        name: 'PaginaReceita',
        component: PaginaReceita
    },
    {
        path: '/EditarPerfil/',
        name: 'EditarPerfil',
        component: EditarPerfil
    },
    {
        path: '/EditarReceita/:id', 
        name: 'EditarReceita',
        component: EditarReceita
    },
    {
        path: '/LoginCadastro/',
        name: 'LoginCadastro',
        component: LoginCadastro
    },
    {
        path: '/Login/',
        name: 'Login',
        component: Login
    },

    {
        path: '/Cadastro/',
        name: 'Cadastro',
        component: Cadastro
    },
    {
        path: '/Perfil/:id', 
        name: 'Perfil',
        component: Perfil
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router