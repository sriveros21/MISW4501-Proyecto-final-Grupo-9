package com.example.sportapp.data.remote.repository

interface StravaRepository {
    fun sendDataStrava (userId: String, callback: SendDataStravaCallback)
    interface SendDataStravaCallback {
        fun onSuccess()
        fun onError(throwable: Throwable)
    }

}