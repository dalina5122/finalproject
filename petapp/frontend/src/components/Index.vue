<template>
    <div>
        <!-- TITLE -->
        <div class="text-info">
            <h1>HOME PAGE</h1>
        </div>

        <!-- BUTTONS -->
        <div>
            <router-link to="/signup" target="_blank">Sign Up</router-link>
            <router-link to="/dogs-map">Dogs Map</router-link>
            <router-link to="/log-in">Log In</router-link>
        </div>
        <router-view></router-view>
</div>
</template>

<script>
// import DogsMap from '../components/DogsMap.vue'
// import SignUp from '../components/SignUp.vue'
// import LogIn from '../components/LogIn.vue'
// export default {
//   components: {
//     DogsMap,
//     SignUp,
//     LogIn
//   }
// }
</script>






