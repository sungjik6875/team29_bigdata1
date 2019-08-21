import Vue from 'vue'
import VueRouter from 'vue-router'
import EmptyPage from '../components/pages/EmptyPage'
import MovieSearchPage from '../components/pages/MovieSearchPage'
import UserInfoPage from '../components/pages/UserInfoPage'
import MovieList from '../components/MovieList'
import MovieDetailPage from '../components/pages/MovieDetailPage'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { 
      path: '/', 
      component: EmptyPage, 
      name: 'home',
      beforeEnter(from, to, next) {
        next('movies/search')
      }
    },
    { 
      path: '/movies/search', 
      component: MovieSearchPage,
      name: 'movie-search' 
    },
    { 
      path: '/userInfo', 
      component: UserInfoPage, 
      name: 'user-info' 
    },
    {
      path: '/movieInfo',
      component: MovieDetailPage,
      name: 'movie-info'
    }
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router