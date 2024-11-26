  <template>
    <div class="min-h-screen bg-gray">
      <NavigationBar />
      <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <HomePageBannerImage />
        <HomePageServiceSection :services="services" />
        <HomePageFriendsSection :friends="friends" />
        <HomePageReviewBoard :reviews="reviews" @reportReview="reportReview" @likeReview="likeReview"
          @toggleComments="toggleComments" @addComment="addComment" />
      </main>
    </div>
  </template>

<script setup>
import { ref } from 'vue'
import NavigationBar from '@/components/NavigationBar.vue'
import HomePageBannerImage from '@/components/HomePageBannerImage.vue'
import HomePageServiceSection from '@/components/HomePageServiceSection.vue'
import HomePageFriendsSection from '@/components/HomePageFriendsSection.vue'
import HomePageReviewBoard from '@/components/HomePageReviewBoard.vue'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const getRandomImages = (count) => {
  return Array(count).fill().map(() => `https://picsum.photos/200/200?random=${Math.random()}`);
};

const services = [
  { name: '예/적금추천', description: '당신에게 딱 맞는 조건의 상품 추천', image: getRandomImages(1), route: '/recommendation' },
  { name: '근처 은행', description: '근처에 은행업무 어디서 보지?', image: getRandomImages(1), route: '/find-bank' },
  { name: '환율 계산기', description: '실시간 환율 계산', image: getRandomImages(1), route: '/currency-exchange' }
]

const friends = [
  { name: 'John Doe', activity: 'Just invested in stocks', avatar: getRandomImages(1) },
  { name: 'Jane Smith', activity: 'Saved $500 this month', avatar: getRandomImages(1) },
  { name: 'Bob Johnson', activity: 'Opened a new savings account', avatar: getRandomImages(1) },
  { name: 'Alice Brown', activity: 'Paid off credit card debt', avatar: getRandomImages(1) }
]

const reviews = ref([
  {
    id: 1,
    name: 'Mike Wilson',
    avatar: getRandomImages(1),
    rating: 5,
    content: 'Great service! The app is easy to use and has helped me save money.',
    likes: 10,
    comments: [
      { id: 1, name: 'Sarah', content: 'I agree! The app is fantastic.' }
    ],
    showComments: false
  },
  {
    id: 2,
    name: 'Emily Davis',
    avatar: getRandomImages(1),
    rating: 4,
    content: 'Good overall, but could use some improvements in the investment section.',
    likes: 5,
    comments: [],
    showComments: false
  }
])

const reportReview = (id) => {
  alert(`Review ${id} reported`)
}

const likeReview = (id) => {
  const review = reviews.value.find(r => r.id === id)
  if (review) {
    review.likes++
  }
}

const toggleComments = (id) => {
  const review = reviews.value.find(r => r.id === id)
  if (review) {
    review.showComments = !review.showComments
  }
}

const addComment = (id, comment) => {
  const review = reviews.value.find(r => r.id === id)
  if (review) {
    review.comments.push({
      id: review.comments.length + 1,
      name: 'You',
      content: comment,
    })
  }
}

onMounted(() => {
  window.addEventListener('message', (event) => {
    if (event.data.type === 'login_success') {
      router.push(event.data.route).then(() => {
        // 라우팅이 완료된 후 새로고침 수행
        setTimeout(() => {
          window.location.reload()
        }, 100)
      })
    }
  })
})
</script>

<style scoped>
</style>