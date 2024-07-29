import axios from 'axios';
import router from '@/router'; 

const state = {
    receitas: [],
    pesquisa: {
        nome_receita: '',
        sabor_receita: [],
        categoria: [],
        dificuldade: '',
        ingredientes: [],
        n_ingredientes: [],
    },
    umedingrediente: [
        {
            letra: 'U',
            valor: 'Unidade'
        },
        {
            letra: 'X',
            valor: 'Xícara de Chá'
        },
        {
            letra: 'C',
            valor: 'Colher de Sopa'
        },
        {
            letra: 'CH',
            valor: 'Colher de Chá'
        },
        {
            letra: 'D',
            valor: 'Dente de Alho'
        },
        {
            letra: 'M',
            valor: 'Mililitro'
        },
        {
            letra: 'L',
            valor: 'Litro'
        },
        {
            letra: 'G',
            valor: 'Gramas'
        },
        {
            letra: 'KG',
            valor: 'Quilogramas'
        },
        {
            letra: 'AGS',
            valor: 'a gosto',
        }
    ],
    saborreceita:[
        {
            letra: 'D',
            valor: 'Doce',
        },
        {
            letra: 'S',
            valor: 'Salgada',
        }
    ],
    tempopreparo:[
        {
            letra: 'M',
            valor: 'Minuto',
        },
        {
            letra: 'H',
            valor: 'Hora',
        },
        {
            letra: 'D',
            valor: 'Dias',
        }
    ],
    categoriareceita:[
        {
            letra: 'C',
            valor: 'Café da manhã',
        },
        {
            letra: 'A',
            valor: 'Almoço',
        },
        {
            letra: 'L',
            valor: 'Lanche',
        },
        {
            letra: 'J',
            valor: 'Janta',
        },
        {
            letra: 'S',
            valor: 'Sobremesas',
        },
        {
            letra: 'B',
            valor: 'Bebidas',
        },
        {
            letra: 'V',
            valor: 'Vegana',
        },
    ],
    dificuldadereceita:[
        {
            letra: 'F',
            valor: 'Fácil',
        },
        {
            letra: 'M',
            valor: 'Médio',
        },
        {
            letra: 'D',
            valor: 'Dificil',
        },
        {
            letra: 'C',
            valor: 'Master Chef',
        }
    ],

};

const getters = {
    allReceitas: state => state.receitas,
    getPesquisa: state => state.pesquisa, 
};

const actions = {
    async fetchReceitas({ commit }) {
        const response = await axios.get(
            '/api/receita/'
        );

        commit ('setReceitas', response.data)
    },
    async basicSearch({ commit, getters }) {
        const response = await axios.get(
            '/api/receita/?nome_receita__icontains=' + getters.getPesquisa.nome_receita
            + '&sabor_receita__in=' + getters.getPesquisa.sabor_receita + '&dificuldade=' + getters.getPesquisa.dificuldade
            + '&categoria__in=' + getters.getPesquisa.categoria
            + '&ingredientes__nome_ingrediente__in=' + getters.getPesquisa.ingredientes
            + '&ingredientes_not=' + getters.getPesquisa.n_ingredientes
        );

        commit ('setReceitas', response.data)
    },

    async deleteReceita({ commit }, id) {
        await axios.delete(`/api/receita/${id}`);
        
        commit('removeReceita', id);
        router.push("/");
    },

    
}

const mutations = {
    setReceitas: (state, receitas) => (state.receitas = receitas),
    removeReceita: (state, id) =>
        (state.receitas = state.receitas.filter(receita => receita.id !== id)),
};

export default {
    state,
    getters,
    actions,
    mutations
};