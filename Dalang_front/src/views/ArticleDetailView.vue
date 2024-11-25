<template>
    <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4" @click="handleBackgroundClick">
        <div v-if="article"
            class="w-full max-w-2xl bg-white rounded-xl shadow-lg overflow-hidden transition-all duration-300 hover:shadow-xl"
            @click.stop>
            <div class="p-8">
                <h1 class="text-4xl font-bold text-gray-900 mb-4">{{ article.title }}</h1>
                <div class="flex items-center justify-between mb-6">
                    <div class="flex items-center">
                        <UserIcon class="h-5 w-5 text-gray-500 mr-2" />
                        <router-link :to="{ name: 'profile', params: { id: article.author } }"
                            class="text-gray-600 hover:text-[#44AAE2] transition-colors">
                            {{ article.author_username }}
                        </router-link>
                    </div>
                    <div class="text-sm text-gray-500">
                        {{ formatDate(article.created_at) }}
                    </div>
                </div>
                <p class="text-gray-700 text-lg leading-relaxed mb-6">{{ article.content }}</p>
                <div class="flex flex-wrap gap-2 mb-6">
                    <span v-for="tag in getTags()" :key="tag"
                        class="bg-gray-200 text-gray-700 px-3 py-1 rounded-full text-sm">
                        {{ tag }}
                    </span>
                </div>
                <div class="flex items-center justify-between text-gray-600">
                    <div class="flex items-center">
                        <button @click="toggleLike" :disabled="article.author === store.userId"
                            class="flex items-center hover:text-[#44AAE2] transition-colors"
                            :class="{ 'text-[#44AAE2]': article.is_liked }">
                            <ThumbsUpIcon class="h-5 w-5 mr-1" />
                            <span>{{ article.like_count }}</span>
                        </button>
                    </div>
                    <button @click="showComments = !showComments"
                        class="flex items-center hover:text-[#44AAE2] transition-colors">
                        <MessageSquareIcon class="h-5 w-5 mr-1" />
                        <span>{{ article.comment_count }}</span>
                    </button>
                </div>
            </div>

            <div v-show="showComments" class="border-t border-gray-200 p-8 transition-all duration-300">
                <h2 class="text-2xl font-bold text-gray-900 mb-4">댓글</h2>

                <!-- 댓글 작성 폼 -->
                <div v-if="store.isLogin" class="mb-6">
                    <textarea v-model="newComment"
                        class="w-full p-3 border rounded-lg focus:ring-2 focus:ring-[#44AAE2] focus:border-transparent"
                        placeholder="댓글을 작성하세요..." rows="3"></textarea>
                    <button @click="submitComment"
                        class="mt-2 px-4 py-2 bg-[#115583] text-white rounded-lg hover:bg-[#44AAE2] transition-colors">
                        댓글 작성
                    </button>
                </div>

                <!-- 댓글 목록 -->
                <div class="space-y-4">
                    <div v-for="comment in comments" :key="comment.id"
                        class="border-b border-gray-100 pb-4 last:border-b-0">
                        <div class="flex justify-between items-start">
                            <div class="flex items-center">
                                <UserIcon class="h-4 w-4 text-gray-500 mr-2" />
                                <router-link :to="{ name: 'profile', params: { id: comment.author } }"
                                    class="font-semibold text-gray-700 hover:text-[#44AAE2]">
                                    {{ comment.author_username }}
                                </router-link>
                            </div>
                            <span class="text-sm text-gray-500">
                                {{ formatDate(comment.created_at) }}
                            </span>
                        </div>
                        <p class="mt-2 text-gray-600">{{ comment.content }}</p>
                    </div>
                </div>
            </div>
        </div>
        <div v-else class="flex items-center justify-center">
            <p>Loading...</p>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router' // useRouter 추가
import axios from 'axios'
import { UserIcon, ThumbsUpIcon, MessageSquareIcon } from 'lucide-vue-next'
const router = useRouter() // router 정의

const handleBackgroundClick = () => {
    router.back()
}
const route = useRoute()
const article = ref(null)

const getTags = () => {
    if (!article.value) return []
    return [
        article.value.hashtag1,
        article.value.hashtag2,
        article.value.hashtag3
    ].filter(tag => tag !== null && tag !== '')
}

const formatDate = (dateString) => {
    if (!dateString) return ''
    return new Intl.DateTimeFormat('ko-KR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    }).format(new Date(dateString))
}

const fetchArticle = async () => {
    try {
        const response = await axios.get(`http://localhost:8000/articles/${route.params.id}/`)
        // 좋아요 상태를 확인하기 위한 별도 요청
        const likedArticlesResponse = await axios.get('http://localhost:8000/articles/liked/', {
            headers: {
                Authorization: `Token ${store.token}`
            }
        })
        // 현재 게시글이 사용자가 좋아요한 게시글 목록에 있는지 확인
        const isLiked = likedArticlesResponse.data.some(article => article.id === response.data.id)
        
        article.value = {
            ...response.data,
            is_liked: isLiked
        }
    } catch (error) {
        console.error('Failed to fetch article:', error)
    }
}

import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const toggleLike = async () => {
    try {
        const response = await axios.post(
            `http://localhost:8000/articles/${route.params.id}/like/`,
            {},
            {
                headers: {
                    Authorization: `Token ${store.token}`
                }
            }
        )
        article.value.is_liked = response.data.liked
        article.value.like_count = response.data.like_count
    } catch (error) {
        console.error('Failed to toggle like:', error)
    }
}
// 댓글 관련 상태 추가
const comments = ref([])
const newComment = ref('')
const showComments = ref(false)

// 댓글 목록 가져오기
const fetchComments = async () => {
    try {
        const response = await axios.get(
            `http://localhost:8000/articles/${route.params.id}/comments/`,
            {
                headers: {
                    Authorization: `Token ${store.token}`
                }
            }
        )
        comments.value = response.data
    } catch (error) {
        console.error('Failed to fetch comments:', error)
    }
}

// 댓글 작성
const submitComment = async () => {
    if (!newComment.value.trim()) return

    try {
        const response = await axios.post(
            `http://localhost:8000/articles/${route.params.id}/comments/create/`,
            { content: newComment.value },
            {
                headers: {
                    Authorization: `Token ${store.token}`
                }
            }
        )
        newComment.value = ''
        await fetchComments() // 댓글 목록을 새로 가져와서 author 정보를 포함한 전체 데이터를 받음
        article.value.comment_count += 1
    } catch (error) {
        console.error('Failed to submit comment:', error)
    }
}
onMounted(() => {
    fetchArticle()
    fetchComments()
})


</script>

<style scoped>
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.min-h-screen {
    animation: fadeIn 0.5s ease-out;
}
</style>