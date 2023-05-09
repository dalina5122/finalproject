<template>
    <div class="container">
      <div class="p-2">
        <div>
            <h4>Which page would you like to visit first?</h4>
            <router-link to="/dogsmap">
                <img loading="auto" src="/media/dogbutton.png" width="100">
            </router-link>
        </div>

        <div>
            <router-link to="/catsmap">
                <img loading="auto" src="/media/catbutton.png" width="100">
            </router-link>
        </div>

        <div>
            <router-link to="/infopage">
                <img loading="auto" src="/media/infobutton.png" width="100">
            </router-link>
        </div>
      </div>
    </div>
</template>