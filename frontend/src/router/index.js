import Vue from 'vue'
import VueRouter from 'vue-router'
import Store from '../store'

import { toastNotification } from '../plugins/vueToast'

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
      redirect: { 
        name: 'movie-search' 
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
      name: 'movie-info',
      async beforeEnter(from, to, next) {
        if (from.query.movieId) {
          await Store._actions['movie/getMovieInfo'][0](from.query);
          next();
        } else {
          toastNotification.$toast.open({
            message: "영화를 선택해주세요",
            type: 'default',
            position: 'top',
          })
          next('/movies/search')
        }
      }
    }
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router