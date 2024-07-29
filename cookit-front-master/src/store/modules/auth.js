const state = {
    user: {
        username: ''
    },
    isAuthenticated: false,
    token: ''
}

const getters = {
    userData: state => state.user,
    isAuthenticated: state => state.isAuthenticated,
    getToken: state => state.token,
}

const mutations = {
    initializeStore(state){
        if(localStorage.getItem('token')){
            state.token = localStorage.getItem('token')
            state.user = localStorage.getItem('user')
            state.isAuthenticated = true
        }
        else{
            state.token = ''
            state.user = ''
            state.isAuthenticated = false
        }
    },
    setToken(state, token) {
        state.token = token
        state.isAuthenticated = true
    },
    removeToken(state){
        state.token = ''
        state.user = ''
        state.isAuthenticated = false
    },
    setUser(state, user){
        state.user = user
    },
}

export default {
    state,
    getters,
    mutations,
}