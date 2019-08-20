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
    { path: '/', component: EmptyPage, name: 'home' },
    { path: '/movies/search', 
      component: MovieSearchPage,
      children: [
        {
          path: 'movieList',
          component: MovieList,
          name: 'movie-list',
          props: true
        },
        {
          path: ':movieId',
          component: MovieDetailPage,
          name: 'movie-detail'
        }
      ],
      name: 'movie-search' 
    },
    { path: '/userInfo', component: UserInfoPage, name: 'user-info' },
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router