import axios from 'axios'

const apiUrl = '/api'

export default {
  searchMovies(params) {
    return axios.get(`${apiUrl}/movies`, {
      params,
    })
  },
  getUserInfo(params) {
    return axios.get(`${apiUrl}/auth/user_info/`, {
      params,
    })
  }
}