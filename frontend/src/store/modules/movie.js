import api from '../../api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  testMessage: '',
}

// actions
const actions = {
  async searchMovies({ commit }, params) {
    const response = await api.searchMovies(params)
    const movies = response.data.map(data => ({
      id: data.id,
      title: data.title,
      genres: data.genres_array,
      viewCnt: data.view_cnt,
      rating: data.average_rating,
    }))
    commit('setMovieSearchList', movies)
  },
}

// mutations
const mutations = {
  setMovieSearchList(state, movies) {
    state.movieSearchList = movies.map(movie => movie)
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}