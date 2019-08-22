<template>
  <div>
    <v-select
      ref="key"
      :items="items"
      label="키워드를 선택하세요."
      solo
    ></v-select>
    <div ref="form">
      <v-text-field v-model="keyword" @keyup.enter="onSubmitByKeyword" label="키워드를 입력하세요." />
      <v-layout justify-center pa-10>
        <v-btn large color="indigo white--text" @click="onSubmitByKeyword">Search</v-btn>
      </v-layout>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    keyword: '',
    items: ['영화명', '장르'],
  }),
  methods: {
    onSubmitByKeyword: function() {
      const key = this.$refs.key.$el.innerText;
      let params;
      if (key.length > 3) {
        alert('키워드를 선택하세요.')
      } else if (key === '영화명') {
        params = {
          title: this.keyword,
          key: "title"
        };
      } else {
        params = {
          genre: this.keyword,
          key: "genre"
        };
      }
      this.$emit('submitByKeyword', params)
    }
  }
};
</script>