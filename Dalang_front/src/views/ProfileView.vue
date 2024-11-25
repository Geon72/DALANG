<template>
  <div class="flex-grow bg-white">
    <NavigationBar :navItems="navItems" />
    <div v-if="loading" class="max-w-5xl mx-auto px-4 py-8">
      Loading profile...
    </div>
    <div v-if="error" class="max-w-5xl mx-auto px-4 py-8">
      {{ error }}
    </div>
    <div v-if="!loading && !error" class="max-w-5xl mx-auto px-4 py-8">
      <ProfileHeader :user="userData" />
      <ProfilePostGrid :myPosts="myPosts" :likedPosts="likedPosts" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import ProfileHeader from '@/components/ProfileHeader.vue'
import ProfilePostGrid from '@/components/ProfilePostGrid.vue'
import NavigationBar from '@/components/NavigationBar.vue'
import { useCounterStore } from '@/stores/counter'

const route = useRoute()
const store = useCounterStore()
const loading = ref(true)
const error = ref(null)

const userData = ref(null)
const myPosts = ref([])
const likedPosts = ref([])

const fetchUserData = async () => {
  try {
    const userId = route.params.id || store.userId;

    if (!userId) {
      throw new Error('User ID is not defined.');
    }

    // 사용자 정보 가져오기 - URL 수정
    const userResponse = await axios.get(`http://localhost:8000/accounts/user/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    userData.value = {
      ...userResponse.data,
      profilePicture: `https://picsum.photos/seed/${userId}/400/400`,
      followers: 0,
      following: 0,
      posts: [],
      fullName: userResponse.data.username,
      bio: ''
    };

    // 내가 쓴 글 가져오기
    const myPostsResponse = await axios.get(`http://localhost:8000/articles/user/${userId}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    myPosts.value = myPostsResponse.data.map(post => ({
      id: post.id,
      title: post.title,
      content: post.content,
      date: new Date(post.created_at).toLocaleDateString(),
      likes: post.like_count,
      comments: post.comment_count,
      image: post.image || `https://picsum.photos/seed/${post.id}/300/300`
    }));

    // userData 업데이트
    userData.value.posts = myPosts.value;

    // 내가 좋아요한 글 가져오기
    const likedPostsResponse = await axios.get(`http://localhost:8000/articles/liked/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    likedPosts.value = likedPostsResponse.data.map(post => ({
      id: post.id,
      title: post.title,
      content: post.content,
      date: new Date(post.created_at).toLocaleDateString(),
      likes: post.like_count,
      comments: post.comment_count,
      image: post.image || `https://picsum.photos/seed/${post.id}/300/300`
    }));
  } catch (err) {
    error.value = err.message;
    console.error('Error:', err);
  } finally {
    loading.value = false;
  }
};
onMounted(() => {
  fetchUserData()
})
</script>

<style scoped></style>