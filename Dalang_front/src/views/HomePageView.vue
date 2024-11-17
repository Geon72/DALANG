<template>
    <div class="min-h-screen bg-white">
      <NavigationBar :navItems="navItems" />
      <HomePageBannerImage />
      <main class="container mx-auto px-4 py-8">
        
        <HomePageServiceSection :services="services" />
        <HomePageFriendsSection :friends="friends" />
        <HomePageReviewBoard :reviews="reviews" @reportReview="reportReview" @likeReview="likeReview" @toggleComments="toggleComments" @addComment="addComment" />
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
  
  const navItems = [
    { name: 'Home', route: '/' },
    { name: 'Personalized Recommendations', route: '/recommendations' },
    { name: 'Find a Bank', route: '/find-bank' },
    { name: 'Currency Calculator', route: '/currency-calculator' },
    { name: 'Community Board', route: '/community' },
  ]
  
  const services = [
    { name: 'Personal Banking', description: 'Manage your finances with ease', image: 'https://placeholders.dev/?width=256&height=192&text=Banking', route: '/personal-banking' },
    { name: 'Investments', description: 'Grow your wealth with smart investments', image: 'https://placeholders.dev/?width=256&height=192&text=Investments', route: '/investments' },
    { name: 'Loans', description: 'Get the financial support you need', image: 'https://placeholders.dev/?width=256&height=192&text=Loans', route: '/loans' }
  ]
  
  const friends = [
    { name: 'John Doe', activity: 'Just invested in stocks', avatar: 'https://placeholders.dev/?width=128&height=128&text=John+Doe' },
    { name: 'Jane Smith', activity: 'Saved $500 this month', avatar: 'https://placeholders.dev/?width=128&height=128&text=Jane+Smith' },
    { name: 'Bob Johnson', activity: 'Opened a new savings account', avatar: 'https://placeholders.dev/?width=128&height=128&text=Bob+Johnson' },
    { name: 'Alice Brown', activity: 'Paid off credit card debt', avatar: 'https://placeholders.dev/?width=128&height=128&text=Alice+Brown' }
  ]
  
  const reviews = ref([
    {
      id: 1,
      name: 'Mike Wilson',
      avatar: 'https://placeholders.dev/?width=40&height=40&text=Mike+Wilson',
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
      avatar: 'https://placeholders.dev/?width=40&height=40&text=Emily+Davis',
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