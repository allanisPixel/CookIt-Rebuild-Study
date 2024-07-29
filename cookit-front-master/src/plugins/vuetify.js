import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import CookitUserIcon from '@/components/icons/CookitUserIcon.vue'
import CookitUserIconCircle from '@/components/icons/CookitUserIconCircle.vue'

Vue.use(Vuetify);

export default new Vuetify({
    theme: {/**/ },
    icons: {
        values: {
            cookit_user: {
                component: CookitUserIcon,
                props: {
                    name: 'cookit_user',
                },
            },
            cookit_user_circle: {
                component: CookitUserIconCircle,
                props: {
                    name: 'cookit_user_circle',
                },
            },
        },
    },
});
