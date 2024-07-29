import Vue from 'vue';
import Vuex from 'vuex';
import receitas from './modules/receitas';
import auth from './modules/auth';

Vue.use(Vuex);

export default new Vuex.Store({
    state:{
        drawer: null,
    },
    modules: {
        receitas,
        auth,
    },
});