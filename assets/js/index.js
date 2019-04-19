window.$ = window.jQuery = require('jquery');
require('bootstrap-sass');
import Vue from 'vue';
import Vuetify from 'vuetify';
import Vuelidate from 'vuelidate';
import VeeValidate from 'vee-validate';

Vue.use(VeeValidate);
Vue.use(Vuelidate);
Vue.use(Vuetify);
import Loot from "./components/Loot.vue";

const app = new Vue({
    el: '#app',
    components: {
        Loot
    }
});