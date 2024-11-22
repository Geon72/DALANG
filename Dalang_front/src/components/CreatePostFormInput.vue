<template>
  <div>
    <label :for="id" class="block text-sm font-medium text-gray-700">{{ label }}</label>
    <input
      :id="id"
      v-bind="$attrs"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
    />
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

defineProps({
  label: {
    type: String,
    required: true
  },
  modelValue: {
    type: String,
    default: ''
  },
  id: {
    type: String,
    default: () => `input-${Math.random().toString(36).substr(2, 9)}`
  }
});

defineEmits(['update:modelValue']);
</script>