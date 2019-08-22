<template>
  <div id="pulse-loader">
    <div class="pulse-loader-1"></div>
    <div class="pulse-loader-2"></div>
  </div>
</template>

<script>
export default {

}
</script>


<style scoped>
.pulse-loader-1, .pulse-loader-2 {
  -webkit-border-radius: 1000px;
  -moz-border-radius: 1000px;
  -o-border-radius: 1000px;
  border-radius: 1000px;
  border-color: #3F51B5;
}

#pulse-loader {
  position: fixed;
  z-index: 100;
  left: 50vw;
  top: 50vh;
  width: 300px;
  height: 300px;
  margin-left: -150px;
  margin-top: -150px;
}

#pulse-loader>div {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-width: 20px;
  border-style: solid;
}

#pulse-loader .pulse-loader-1 {
  -webkit-animation: pulse1 1s .5s ease infinite;
  -moz-animation: pulse1 1s .5s ease infinite;
  -ms-animation: pulse1 1s .5s ease infinite;
  -o-animation: pulse1 1s .5s ease infinite;
  animation: pulse1 1s .5s ease infinite
}

#pulse-loader .pulse-loader-2 {
  -webkit-animation: pulse1 1s ease infinite;
  -moz-animation: pulse1 1s ease infinite;
  -ms-animation: pulse1 1s ease infinite;
  -o-animation: pulse1 1s ease infinite;
  animation: pulse1 1s ease infinite
}

@-webkit-keyframes pulse1 {
  0% {
    -webkit-transform: scale(0)
  }
  40% {
    -webkit-transform: scale(0.3);
    opacity: 1
  }
  100% {
    -webkit-transform: scale(1);
    opacity: 0
  }
}

@-moz-keyframes pulse1 {
  0% {
    -moz-transform: scale(0)
  }
  40% {
    -moz-transform: scale(0.3);
    opacity: 1
  }
  100% {
    -moz-transform: scale(1);
    opacity: 0
  }
}

@-o-keyframes pulse1 {
  0% {
    -o-transform: scale(0)
  }
  40% {
    -o-transform: scale(0.3);
    opacity: 1
  }
  100% {
    -o-transform: scale(1);
    opacity: 0
  }
}

@-ms-keyframes pulse1 {
  0% {
    -ms-transform: scale(0)
  }
  40% {
    -ms-transform: scale(0.3);
    opacity: 1
  }
  100% {
    -ms-transform: scale(1);
    opacity: 0
  }
}

@keyframes pulse1 {
  0% {
    transform: scale(0)
  }
  40% {
    transform: scale(0.3);
    opacity: 1
  }
  100% {
    transform: scale(1);
    opacity: 0
  }
}
</style>