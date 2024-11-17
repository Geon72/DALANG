<template>
    <div class="p-4 flex justify-end">
      <button 
        @click="handleExport" 
        class="flex items-center px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600 transition-colors"
      >
        <DocumentArrowDownIcon class="w-5 h-5 mr-2" />
        Excel로 출력
      </button>
    </div>
</template>
  
<script setup>
import { DocumentArrowDownIcon } from '@heroicons/vue/24/outline'
import ExcelJS from 'exceljs'
  
const props = defineProps({
  data: {
    type: Array,
    required: true
  },
  headers: {
    type: Array,
    required: true
  },
  tabType: {  // 새로운 prop 추가
    type: String,
    required: true
  }
})
  
const handleExport = async () => {
  const workbook = new ExcelJS.Workbook()
  const worksheetName = props.tabType === '정기적금' ? '적금상품비교' : '예금상품비교'
  const worksheet = workbook.addWorksheet(worksheetName)

  // 헤더 설정
  worksheet.columns = props.headers.map(header => ({
    header: header,
    key: header,
    width: 15
  }))

  // 스타일 설정
  worksheet.getRow(1).font = { bold: true }
  worksheet.getRow(1).fill = {
    type: 'pattern',
    pattern: 'solid',
    fgColor: { argb: 'FFE6F0FF' }
  }

  // 데이터 추가
  props.data.forEach(item => {
    worksheet.addRow(item)
  })

  // 파일 다운로드
  const buffer = await workbook.xlsx.writeBuffer()
  const blob = new Blob([buffer], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' })
  const url = window.URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url
  link.download = `${worksheetName}.xlsx`
  link.click()
  window.URL.revokeObjectURL(url)
}
</script>