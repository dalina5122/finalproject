<template>
    <div>
      <header class="header-background">
        <div>
          <router-link to="/">
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

.header-background{
  background-image: url('/media/paws.gif');
  background-position: center;
  background-repeat: no-repeat;
  background-size: 100% auto; 
  width: 1000px;
  height: 100%;
}

</style>