<template>
    <div class="bg-[#F5F5F5] min-h-screen py-8 px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold text-[#115583] mb-8">마음에 드는 채널을 골라보세요</h1>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div v-for="channel in channels" :key="channel.hashtag" class="bg-white rounded-lg shadow-md p-4">
          <div class="flex justify-between items-center mb-3">
            <div>
              <h2 class="text-lg font-bold text-[#115583]">{{ channel.hashtag }}</h2>
              <p class="text-xs text-[#4A524D]">{{ channel.followers }}명 팔로우 중 · {{ channel.posts }}개의 게시물</p>
            </div>
            <button 
              class="text-[#44AAE2] hover:text-[#115583] transition-colors duration-200" 
              aria-label="더 보기"
            >
              <ChevronRight class="w-5 h-5" />
            </button>
          </div>
  
          <div class="relative">
            <div class="flex overflow-x-auto gap-3 snap-x snap-mandatory scrollbar-hide pb-3">
              <div 
                v-for="(image, index) in channel.images" 
                :key="index" 
                class="flex-none w-[200px] first:ml-0 snap-start"
              >
                <div class="aspect-square rounded-lg overflow-hidden">
                  <img 
                    :src="image" 
                    :alt="`${channel.hashtag} 이미지 ${index + 1}`" 
                    class="w-full h-full object-cover transition-transform duration-200 hover:scale-105"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ChevronRight } from 'lucide-vue-next';
  
  const getRandomImages = (count) => {
    return Array(count).fill().map(() => `https://picsum.photos/200/200?random=${Math.random()}`);
  };
  
  const channels = [
    {
      hashtag: '#재테크초보',
      followers: '4,688',
      posts: '11,617',
      images: getRandomImages(6)
    },
    {
      hashtag: '#월급관리',
      followers: '888',
      posts: '1,013',
      images: getRandomImages(6)
    },
    {
      hashtag: '#청년재테크',
      followers: '2,164',
      posts: '28,081',
      images: getRandomImages(6)
    },
    {
      hashtag: '#주식초보',
      followers: '408',
      posts: '2,475',
      images: getRandomImages(6)
    },
    {
      hashtag: '#신혼부부대출',
      followers: '16516',
      posts: '74,132',
      images: getRandomImages(6)
    },
    {
      hashtag: '#신혼통장',
      followers: '4412',
      posts: '4,874',
      images: getRandomImages(6)
    }
  ];
  </script>
  
  <style scoped>
  .scrollbar-hide {
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
  .scrollbar-hide::-webkit-scrollbar {
    display: none;
  }
  
  .snap-x {
    scroll-behavior: smooth;
  }
  </style>