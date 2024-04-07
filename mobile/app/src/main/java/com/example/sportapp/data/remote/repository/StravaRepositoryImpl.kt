package com.example.sportapp.data.remote.repository

import com.example.sportapp.data.remote.api.ApiService
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class StravaRepositoryImpl(private val apiService: ApiService) : StravaRepository {


    override fun sendDataStrava(userId: String, callback: StravaRepository.SendDataStravaCallback) {

        val call = apiService.sendDataStrava(userId) //Parametros del servicio

/*        if (call != null) {
            call.enqueue(object : Callback<Void> {
                override fun onResponse(call: Call<Void>, response: Response<Void>) {
                    if (response.isSuccessful) {
                        callback.onSuccess()
                    } else {
                        callback.onError(Exception("Error en la llamada"))
                    }
                }

                override fun onFailure(call: Call<Void>, t: Throwable) {
                    callback.onError(t)
                }
            })
        }*/
    }
}
