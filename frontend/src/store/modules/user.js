import api from '../../api'


const state = {
  userInfo: {}
}

const mutations = {
  setUserInfo(state, userInfo) {
    state.userInfo = userInfo
  }
}

const actions = {
  async getUserInfo({ commit }, params) {
    const response = await api.getUserInfo(params)
    console.log(response.data)
    const userInfo = {
      id: response.data.id,
      username: response.data.username,
      gender: response.data.gender,
      age: response.data.age,
      occupation: response.data.occupation,
      movies: response.data.movies || []
    }
    commit('setUserInfo', userInfo)
  }
}


export default {
  namespaced: true,
  state,
  actions,
  mutations
}