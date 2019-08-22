const state = {
  isLoading: false
}

const mutations = {
  switchLoader(state) {
    state.isLoading = !state.isLoading;
  }
}

export default {
  namespaced: true,
  state,
  mutations
}