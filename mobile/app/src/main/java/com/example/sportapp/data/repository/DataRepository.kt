package com.example.sportapp.data.repository

import android.util.Log
import com.example.sportapp.SportApp
import com.example.sportapp.data.api.CalculateFTPVo2Service
import com.example.sportapp.data.api.EventsService
import com.example.sportapp.data.api.ReceiveSesionDataService
import com.example.sportapp.data.api.StartTrainingService
import com.example.sportapp.data.api.StopTrainingService
import com.example.sportapp.data.model.CalculateFtpVo2maxRequest
import com.example.sportapp.data.model.ReceiveSesionDataRequest
import com.example.sportapp.data.model.ReceiveSesionDataResponse
import com.example.sportapp.data.model.StartTrainingRequest
import com.example.sportapp.data.model.StartTrainingResponse
import com.example.sportapp.data.model.StopTrainingRequest
import com.example.sportapp.data.model.StopTrainingResponse
import com.example.sportapp.data.model.TrainingMetricsCalculatedResponse
import com.google.gson.Gson
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.RequestBody.Companion.toRequestBody
import retrofit2.Callback
import java.util.Date


class DataRepository(private val apiService: EventsService) {
    fun getCalendarEvents(userId: Int) = apiService.getCalendarEvents(userId)
}

class FTPVO2Repository(private val ftpVo2Service: CalculateFTPVo2Service) {
    fun postCalculateFTPVo2(sessionId: String, callback: Callback<TrainingMetricsCalculatedResponse>) {
        val calculateFtpVo2maxRequest = CalculateFtpVo2maxRequest(sessionId)
        val jsonRequest = Gson().toJson(calculateFtpVo2maxRequest)
        Log.d("DEBUG",  "Data en Respository Body > " + jsonRequest.toString() + " Sesion -> " + sessionId)
        val requestBody1 = jsonRequest.toString().toRequestBody("application/json".toMediaTypeOrNull())
        Log.d("DEBUG",  "Data en Respository Body -- 1 > " + requestBody1.toString() + " Sesion -> " + sessionId)
        ftpVo2Service.postCalculateFTPVo2Service(requestBody1).enqueue(callback)
    }
}

class StartTrainingRepository(private val startTrainingService: StartTrainingService) {
    fun startTrainingService(userId: Int, trainingType: String, callback: Callback<StartTrainingResponse>) {
        val startTrainingRequest = StartTrainingRequest(user_id = userId, training_type = trainingType)
        val jsonRequest = Gson().toJson(startTrainingRequest)
        val requestBody = jsonRequest.toRequestBody("application/json".toMediaTypeOrNull())
        startTrainingService.startTrainingService(requestBody).enqueue(callback)
    }
}

class StopTrainingRepository(private val stopTrainingService: StopTrainingService) {
    fun stopTrainingService(sesionId: String, trainingDate: Date, duration: Int, caloriesBurned: Int, notes: String, callback: Callback<StopTrainingResponse>) {
        val stopTrainingRequest = StopTrainingRequest(session_id = sesionId, end_time = trainingDate, duration = duration, calories_burned = caloriesBurned, notes = notes)
        val jsonRequest = Gson().toJson(stopTrainingRequest)
        val requestBody = jsonRequest.toRequestBody("application/json".toMediaTypeOrNull())
        stopTrainingService.stopTrainingService(requestBody).enqueue(callback)
    }
}

class ReceiveSesionDataRepository(private val receiveSesionDataService: ReceiveSesionDataService) {
    fun receiveSesionDataService(sesionId: String, powerOutput: Int, maxHeartRate: Int, restingHeartRate: Int, callback: Callback<ReceiveSesionDataResponse>) {
        val stopTrainingRequest = ReceiveSesionDataRequest(session_id = sesionId, power_output = powerOutput, max_heart_rate = maxHeartRate, resting_heart_rate = restingHeartRate)
        val jsonRequest = Gson().toJson(stopTrainingRequest)
        val requestBody = jsonRequest.toRequestBody("application/json".toMediaTypeOrNull())
        receiveSesionDataService.receiveSesionDataServiceService(requestBody).enqueue(callback)
    }
}