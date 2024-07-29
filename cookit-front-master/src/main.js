import Vue from 'vue'
import App from './App.vue'
// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import router from './router'
import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'
import VueHighlightJS from 'vue-highlightjs'
import store from './store'
import axios from 'axios'
import vuetify from './plugins/vuetify'

Vue.use(VueHighlightJS);

Vue.config.productionTip = false

axios.defaults.baseURL = document.location.protocol + "//" + document.location.hostname + ':' + '8000'

console.log("axios.defaults.baseURL = " + axios.defaults.baseURL)

new Vue({
  store,
  router,
  axios,
  vuetify,
  render: h => h(App)
}).$mount('#app')
