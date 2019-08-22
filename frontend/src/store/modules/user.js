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
    try {
      commit('app/switchLoader', null, { root: true })
      const response = await api.getUserInfo(params)
      const userInfo = {
        id: response.data.id,
        username: response.data.username,
        gender: response.data.gender,
        age: response.data.age,
        occupation: response.data.occupation,
        movies: response.data.movies || []
      }
      commit('app/switchLoader', null, { root: true })
      commit('setUserInfo', userInfo)
    } catch(error) {
      console.log("Failed in getting Information about User", error);
      const userInfo = {
        username: null
      }
      commit('setUserInfo', userInfo)
    }   
  }
}


export default {
  namespaced: true,
  state,
  actions,
  mutations
}