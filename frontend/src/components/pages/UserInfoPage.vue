<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>

      <!-- 검색 폼 -->
      <v-flex xs6>
        <div class="display-2 pa-10">사용자 찾기</div>
        <v-form ref="form">
          <v-text-field type="number" v-model="keyword" label="사용자 번호"/>
          <v-layout justify-center pa-10>
            <v-btn large color="indigo white--text" @click="searchUserInfo">Search</v-btn>
          </v-layout>
        </v-form>
      </v-flex>
      
      <!-- 검색 결과 -->
      <v-flex xs7>
        <user-info-box
          :username="userInfo.username"
          :gender="userInfo.gender"
          :age="userInfo.age"
          :occupation="userInfo.occupation"
          :movies="userInfo.movies"
        />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import UserInfoBox from '../UserInfoBox'


export default {
  data() {
    return {
      keyword: ""
    }
  },
  components: {
    UserInfoBox
  },
  computed: {
    ...mapState({
      userInfo: state => state.user.userInfo
    })
  },
  methods: {
    ...mapActions('user', ['getUserInfo']),
    searchUserInfo() {
      const params = {
        userId: this.keyword
      }
      this.getUserInfo(params)
    }
  }
}
</script>

<style scoped>

</style>