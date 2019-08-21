import api from '../../api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  testMessage: '',

  userListForMovie: []
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
  async getMovieInfo({ commit }, params) {
    const { data: { users }} = await api.getMovieInfo(params)
    // console.log(users)
    commit('setUserListForMovie', users)
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
  setUserListForMovie(state, users) {
    state.userListForMovie = users.map(user => user)
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}