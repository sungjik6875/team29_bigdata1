import api from '../../api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  testMessage: '',

  movieInfo: {}
}

// actions
const actions = {
  async searchMovies({ commit }, params) {
    try{
      commit('app/switchLoader', null, { root: true })
      const response = await api.searchMovies(params)
      const movies = response.data.map(data => ({
        id: data.id,
        title: data.title,
        genres: data.genres_array,
        viewCnt: data.view_cnt,
        rating: data.average_rating,
      }))
      commit('app/switchLoader', null, { root: true })
      commit('setMovieSearchList', movies)
    } catch(error) {
      console.log("Failed in searching Movies", error)
    }   
  },
  async getMovieInfo({ commit }, params) {
    try {
      commit('app/switchLoader', null, { root: true })
      const { data } = await api.getMovieInfo(params)
      commit('app/switchLoader', null, { root: true })
      commit('setMovieInfo', data)
    } catch(error) {
      console.log("Failed in getting Infomation about the Movie", error)
    }
    
  }
}

// mutations
const mutations = {
  setMovieSearchList(state, movies) {
    state.movieSearchList = movies.map(movie => movie)
  },
  sortMovies(state, key) {
    
    if (key === 'v') {
      state.movieSearchList = state.movieSearchList.sort((a, b) => {
        return a.viewCnt > b.viewCnt ? -1 : a.viewCnt < b.viewCnt ? 1 : 0;
      })
    }

    if (key === 'r') {
      state.movieSearchList = state.movieSearchList.sort((a, b) => {
        return a.rating > b.rating ? -1 : a.rating < b.rating ? 1 : 0;
      })
    }
  },
  setMovieInfo(state, movieInfo) {
    state.movieInfo = movieInfo 
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}