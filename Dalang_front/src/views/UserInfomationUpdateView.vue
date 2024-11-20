<template>
    <div class="flex-grow bg-gray">
        <NavigationBar/>
        <div class="max-w-5xl mx-auto px-4 py-8">
            <UserInfomationUpdate />
        </div>
    </div>
</template>

<script setup>
import NavigationBar from '@/components/NavigationBar.vue'
import UserInfomationUpdate from '@/components/UserInfomationUpdate.vue'
</script>