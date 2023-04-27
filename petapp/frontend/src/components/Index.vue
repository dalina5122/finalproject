<template>
    <div class="container">

      <!-- TITLE -->
      <div class="text-info">
        <h1>Welcome to App Name</h1>
      </div>
  
      <!-- BUTTONS -->
      <div class="p-2">
        <!-- CREATE ACCOUNT -->
        <div>
            <h4>Would you like to create an account?</h4>
            <router-link to="/signup">
                <img loading="auto" src="/media/signup.png" width="100">
            </router-link>
        </div>

        <!-- LOG IN -->
        <div>
            <h4>Already have an account?</h4>
            <router-link to="/log-in">
                <img loading="auto" src="/media/login.png" width="100">
            </router-link>
        </div>

        <!-- ARROW FOR SCROLLING DOWN -->
        <div class="fixed-bottom d-flex align-items-end justify-content-end">
                <img loading="auto" src="/media/arrow.gif" width="100">
        </div>
      </div>
    </div>
</template>

<script>

</script>






