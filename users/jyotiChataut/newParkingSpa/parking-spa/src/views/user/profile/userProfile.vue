<template>
  <div class="h-full bg-gray-200 p-8">
    <div class="bg-white rounded-lg shadow-xl pb-8">
      <div
        x-data="{ openSettings: false }"
        class="absolute right-12 mt-4 rounded"
      >
        <button
          @click="openSettings = !openSettings"
          class="border border-gray-400 p-2 rounded text-gray-300 hover:text-gray-300 bg-gray-100 bg-opacity-10 hover:bg-opacity-20"
          title="Settings"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-4 w-4"
            fill="currentColor"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="3"
              d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z"
            ></path>
          </svg>
        </button>
        <div
          x-show="openSettings"
          @click.away="openSettings = false"
          class="bg-white absolute right-0 w-40 py-2 mt-1 border border-gray-200 shadow-2xl"
          style="display: none"
        >
          <div class="py-2 border-b">
            <p class="text-gray-400 text-xs px-6 uppercase mb-1">Settings</p>
            <button
              class="w-full flex items-center px-6 py-1.5 space-x-2 hover:bg-gray-200"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-4 w-4 text-gray-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"
                ></path>
              </svg>
              <span class="text-sm text-gray-700">Share Profile</span>
            </button>
            <button
              class="w-full flex items-center py-1.5 px-6 space-x-2 hover:bg-gray-200"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-4 w-4 text-gray-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636"
                ></path>
              </svg>
              <span class="text-sm text-gray-700">Block User</span>
            </button>
            <button
              class="w-full flex items-center py-1.5 px-6 space-x-2 hover:bg-gray-200"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-4 w-4 text-gray-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                ></path>
              </svg>
              <span class="text-sm text-gray-700">More Info</span>
            </button>
          </div>
          <div class="py-2">
            <p class="text-gray-400 text-xs px-6 uppercase mb-1">Feedback</p>
            <button
              class="w-full flex items-center py-1.5 px-6 space-x-2 hover:bg-gray-200"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-4 w-4 text-gray-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
                ></path>
              </svg>
              <span class="text-sm text-gray-700">Report</span>
            </button>
          </div>
        </div>
      </div>
      <div class="w-full h-[250px]">
        <img
          src="https://vojislavd.com/ta-template-demo/assets/img/profile-background.jpg"
          class="w-full h-full rounded-tl-lg rounded-tr-lg"
        />
      </div>
      <div class="flex flex-col items-center -mt-20">
        <img
          src="https://vojislavd.com/ta-template-demo/assets/img/profile.jpg"
          class="w-40 border-4 border-white rounded-full"
        />
        <div class="flex items-center space-x-2 mt-2">
          <p class="text-2xl">Jyoti Chataut</p>
          <span class="bg-blue-500 rounded-full p-1" title="Verified">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="text-gray-100 h-2.5 w-2.5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="4"
                d="M5 13l4 4L19 7"
              ></path>
            </svg>
          </span>
        </div>
      </div>
      <div
        class="flex-1 flex flex-col items-center lg:items-end justify-end px-8 mt-2"
      >
        <div class="flex items-center space-x-4 mt-2"></div>
      </div>
    </div>

    <div
      class="my-4 flex flex-col 2xl:flex-row space-y-4 2xl:space-y-0 2xl:space-x-4"
    >
      <div class="w-full flex flex-col md:flex-row 2xl:w-1/3">
        <div class="flex-1 bg-white rounded-lg shadow-xl p-8 mr-2">
          <h4 class="text-xl text-gray-900 font-bold">Personal Info</h4>
          <ul class="mt-2 text-gray-700">
            <li class="flex border-y py-2">
              <span class="font-bold w-24">Full name:</span>
              <span class="text-gray-700">Test User</span>
            </li>
            <li class="flex border-b py-2">
              <span class="font-bold w-24">Birthday:</span>
              <span class="text-gray-700">24 Jun, 1997</span>
            </li>
            <li class="flex border-b py-2">
              <span class="font-bold w-24">Joined:</span>
              <span class="text-gray-700">10 Jan 2023</span>
            </li>
            <li class="flex border-b py-2">
              <span class="font-bold w-24">Mobile:</span>
              <span class="text-gray-700">+977 575963</span>
            </li>
            <li class="flex border-b py-2">
              <span class="font-bold w-24">Email:</span>
              <span class="text-gray-700">testtest@gmail.com</span>
            </li>
            <li class="flex border-b py-2">
              <span class="font-bold w-24">Location:</span>
              <span class="text-gray-700">Kathmandu, Nepal</span>
            </li>
            <li class="flex border-b py-2">
              <span class="font-bold w-24">Languages:</span>
              <span class="text-gray-700">English, Nepali</span>
            </li>
            <li class="flex items-center border-b py-2 space-x-2">
              <span class="font-bold w-24">Elsewhere:</span>
            </li>
          </ul>
        </div>
        <div class="flex-1 bg-white rounded-lg shadow-xl p-8 ml-2">
          <h4 class="text-xl text-gray-900 font-bold">Parking History</h4>
          <div class="relative px-4">
            <div
              class="absolute h-full border border-dashed border-opacity-20 border-secondary"
            ></div>

            <div class="flex items-center w-full my-6 -ml-1.5">
              <div class="w-1/12 z-10">
                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
              </div>
              <div class="w-11/12">
                <p class="text-sm">Profile informations changed.</p>
                <p class="text-xs text-gray-500">3 min ago</p>
              </div>
            </div>

            <div class="flex items-center w-full my-6 -ml-1.5">
              <div class="w-1/12 z-10">
                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
              </div>
              <div class="w-11/12">
                <p class="text-sm">
                  Connected with
                  <a href="#" class="text-blue-600 font-bold">Colby Covington</a
                  >.
                </p>
                <p class="text-xs text-gray-500">15 min ago</p>
              </div>
            </div>

            <div class="flex items-center w-full my-6 -ml-1.5">
              <div class="w-1/12 z-10">
                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
              </div>
              <div class="w-11/12">
                <p class="text-sm">
                  Invoice
                  <a href="#" class="text-blue-600 font-bold">#4563</a> was
                  created.
                </p>
                <p class="text-xs text-gray-500">57 min ago</p>
              </div>
            </div>

            <div class="flex items-center w-full my-6 -ml-1.5">
              <div class="w-1/12 z-10">
                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
              </div>
              <div class="w-11/12">
                <p class="text-sm">
                  Message received from
                  <a href="#" class="text-blue-600 font-bold">Cecilia Hendric</a
                  >.
                </p>
                <p class="text-xs text-gray-500">1 hour ago</p>
              </div>
            </div>
            <div class="flex items-center w-full my-6 -ml-1.5">
              <div class="w-1/12 z-10">
                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
              </div>
              <div class="w-11/12">
                <p class="text-sm">
                  New order received
                  <a href="#" class="text-blue-600 font-bold">#OR9653</a>.
                </p>
                <p class="text-xs text-gray-500">2 hours ago</p>
              </div>
            </div>
            <div class="flex items-center w-full my-6 -ml-1.5">
              <div class="w-1/12 z-10">
                <div class="w-3.5 h-3.5 bg-blue-600 rounded-full"></div>
              </div>
              <div class="w-11/12">
                <p class="text-sm">
                  Message received from
                  <a href="#" class="text-blue-600 font-bold">Jane Stillman</a>.
                </p>
                <p class="text-xs text-gray-500">2 hours ago</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>
