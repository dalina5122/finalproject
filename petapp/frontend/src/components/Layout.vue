<template>
  <div>
    <header class="header-background">
      <div class="header-content">
        <router-link to="/menupage">
          <div>
            <img loading="auto" src="/media/logo.png" width="300">
          </div>
        </router-link>
      </div>
    </header>
    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<style scoped>
  .header-background {
    background-image: url('/media/paws.gif');
    background-position: center;
    background-repeat: no-repeat;
    background-size: 100% auto;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
  }
</style>
