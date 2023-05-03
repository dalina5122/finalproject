<template>
    <div class="dogs-comments">
      <h3>Comments</h3>
      <div v-for="comment in comments" :key="comment.id" class="comment">
        <p>
          <strong>{{ comment.user.username }}</strong>: {{ comment.content_d }}
        </p>
        <small>{{ comment.timestamp_d }}</small>
      </div>
  
      <div v-if="authenticated">
        <form @submit.prevent="submitComment">
          <label for="content_d">Add a comment:</label>
          <textarea id="content_d" v-model="newComment" required></textarea>
          <button type="submit">Submit</button>
        </form>
      </div>
      <div v-else>
        <p>Please log in to post a comment.</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    props: {
      dogId: {
        type: Number,
        required: true,
      },
    },
    data() {
      return {
        comments: [],
        newComment: "",
        authenticated: false,
      };
    },
    async created() {
      this.authenticated = localStorage.getItem("token") !== null;
      await this.fetchComments();
    },
    methods: {
      async fetchComments() {
        try {
          const response = await axios.get("http://127.0.0.1:8000/petapp/dogscomments/", {
            params: { dog_id: this.dogId },
          });
          this.comments = response.data;
        } catch (error) {
          console.error("Error fetching comments:", error);
        }
      },
      async submitComment() {
        if (!this.newComment.trim()) return;
  
        try {
          const headers = {
            "Content-Type": "application/json",
            Authorization: `Token ${localStorage.getItem("token")}`,
          };
  
          const response = await axios.post(
            "http://127.0.0.1:8000/petapp/dogscomments/",
            {
              dog_id: this.dogId,
              content_d: this.newComment,
            },
            { headers }
          );
  
          this.comments.push(response.data);
          this.newComment = "";
        } catch (error) {
          console.error("Error submitting comment:", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  