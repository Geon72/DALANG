<template>
  <div class="map-container">
    <div id="map" ref="mapContainer" class="map"></div>
    <button 
      @click="findCurrentLocation" 
      class="location-button flex items-center gap-2 bg-white hover:bg-gray-50 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow"
    >
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />
      </svg>
      내 위치 찾기
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const KAKAO_MAP_API_KEY = import.meta.env.VITE_KAKAO_MAP_API_KEY

const props = defineProps({
  selectedType: {
    type: String,
    default: 'ALL'
  },
  selectedRadius: {
    type: String,
    default: '1000'
  }
})

const emit = defineEmits(['update:banks'])
const mapContainer = ref(null)
const map = ref(null)
const ps = ref(null)
const infowindow = ref(null)
const markers = ref([])
const currentPositionMarker = ref(null)

// 마커 이미지 변수 선언
let bankMarkerImage = null
let atmMarkerImage = null
let currentLocationMarkerImage = null

const findCurrentLocation = () => {
  if (!navigator.geolocation) {
    alert("이 브라우저에서는 위치 정보를 지원하지 않습니다.")
    return
  }

  navigator.geolocation.getCurrentPosition(
    (position) => {
      const lat = position.coords.latitude
      const lon = position.coords.longitude
      const locPosition = new window.kakao.maps.LatLng(lat, lon)
      
      displayCurrentPositionMarker(locPosition)
      map.value.setCenter(locPosition)
      searchNearbyBanks(locPosition)
    },
    (error) => {
      console.error("Error getting current location:", error)
      alert("현재 위치를 가져올 수 없습니다. 오류: " + error.message)
    },
    {
      enableHighAccuracy: true,
      timeout: 10000,
      maximumAge: 0
    }
  )
}

const displayCurrentPositionMarker = (locPosition) => {
  if (currentPositionMarker.value) {
    currentPositionMarker.value.setMap(null)
  }
  
  currentPositionMarker.value = new window.kakao.maps.Marker({
    map: map.value,
    position: locPosition,
    image: currentLocationMarkerImage
  })
}

const searchNearbyBanks = (locPosition) => {
  const searchKeyword = props.selectedType === 'ATM' ? 'ATM' : 
                       props.selectedType === 'BANK' ? '은행' : '은행 ATM'
  
  const searchOptions = {
    location: locPosition,
    radius: parseInt(props.selectedRadius),
    sort: window.kakao.maps.services.SortBy.DISTANCE
  }

  ps.value.keywordSearch(searchKeyword, (data, status) => {
    if (status === window.kakao.maps.services.Status.OK) {
      const bounds = new window.kakao.maps.LatLngBounds()
      const banksData = data
        .filter(place => {
          if (props.selectedType === 'ALL') return true
          const isAtm = place.place_name.toLowerCase().includes('atm')
          return props.selectedType === 'ATM' ? isAtm : !isAtm
        })
        .map(place => ({
          id: place.id,
          name: place.place_name,
          type: place.place_name.toLowerCase().includes('atm') ? 'ATM' : 'BANK',
          distance: place.distance,
          address: place.address_name,
          isOpen: true,
          hours: '9:00 - 16:00',
          position: new window.kakao.maps.LatLng(place.y, place.x)
        }))

      removeMarkers()
      banksData.forEach(bank => {
        displayMarker(bank)
        bounds.extend(bank.position)
      })
      
      // 현재 위치도 경계에 포함
      bounds.extend(locPosition)
      
      // 검색 결과가 있을 때만 지도 영역 재설정
      if (banksData.length > 0) {
        map.value.setBounds(bounds)
      }
      
      emit('update:banks', banksData)
    }
  }, searchOptions)
}

const initMap = () => {
  if (!mapContainer.value) {
    console.error('Map container not found')
    return
  }

  try {
    const options = {
      center: new window.kakao.maps.LatLng(37.566826, 126.9786567),
      level: 3
    }
    
    map.value = new window.kakao.maps.Map(mapContainer.value, options)
    ps.value = new window.kakao.maps.services.Places()
    infowindow.value = new window.kakao.maps.InfoWindow({ zIndex: 1 })

    // 마커 이미지 초기화 - 상대 경로 대신 절대 URL 사용
    bankMarkerImage = new window.kakao.maps.MarkerImage(
      'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png', // 은행 마커
      new window.kakao.maps.Size(24, 35)
    )
    atmMarkerImage = new window.kakao.maps.MarkerImage(
      'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_red.png', // ATM 마커
      new window.kakao.maps.Size(24, 35)
    )
  } catch (error) {
    console.error('Error initializing map:', error)
  }
}

const displayMarker = (place) => {
  const markerImage = place.type === 'ATM' ? atmMarkerImage : bankMarkerImage
  
  const marker = new window.kakao.maps.Marker({
    map: map.value,
    position: place.position,
    image: markerImage
  })

  window.kakao.maps.event.addListener(marker, 'click', () => {
    infowindow.value.setContent(`
      <div style="padding:5px;font-size:12px;">
        ${place.name}<br>
        ${place.address}
      </div>
    `)
    infowindow.value.open(map.value, marker)
  })

  markers.value.push(marker)
}

const removeMarkers = () => {
  for (let i = 0; i < markers.value.length; i++) {
    markers.value[i].setMap(null)
  }
  markers.value = []
}

const loadKakaoMap = () => {
  return new Promise((resolve, reject) => {
    if (window.kakao && window.kakao.maps) {
      resolve()
    } else {
      const script = document.createElement('script')
      script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${KAKAO_MAP_API_KEY}&libraries=services&autoload=false`
      script.async = true
      
      script.onload = () => {
        window.kakao.maps.load(() => {
          resolve()
        })
      }
      
      script.onerror = (error) => {
        reject(error)
      }
      
      document.head.appendChild(script)
    }
  })
}

onMounted(async () => {
  try {
    await loadKakaoMap()
    initMap()
    findCurrentLocation()
  } catch (error) {
    console.error('카카오맵 로드 실패:', error)
    alert('지도를 불러오는데 실패했습니다. 페이지를 새로고침해주세요.')
  }
})

defineExpose({
  findCurrentLocation,
  searchNearbyBanks
})
</script>

<style scoped>
.map-container {
  width: 100%;
  height: 500px;
  position: relative;
  border-radius: 8px;
  overflow: hidden;
}

.map {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.location-button {
  position: absolute;
  top: 10px;
  right: 10px;
  z-index: 2;
}
</style>