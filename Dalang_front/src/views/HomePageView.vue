  <template>
    <div class="min-h-screen bg-white">
      <NavigationBar />
      <HomePageBannerImage/>
      <main class="container mx-auto px-4 py-8">
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

const getRandomImages = (count) => {
    return Array(count).fill().map(() => `https://picsum.photos/200/200?random=${Math.random()}`);
  };

const services = [
  { name: '예/적금추천', description: '형님에게 딱 맞는 조건의 상품 추천', image: getRandomImages(1), route: '/recommendation' },
  { name: '근처 은행', description: '돈 인출해야하는데 어딨냐', image: getRandomImages(1), route: '/find-bank' },
  { name: '환율 계산기', description: '실시간 환율 계산 - 특: 아님', image: getRandomImages(1), route: '/currency-exchange' }
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
</script>