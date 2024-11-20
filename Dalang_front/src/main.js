import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

// FontAwesome 설정 -seok
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
// FontAwesome 설정 -seok

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
// FontAwesome 설정 -seok
app.component('font-awesome-icon', FontAwesomeIcon)
// FontAwesome 설정 -seok
app.mount('#app')