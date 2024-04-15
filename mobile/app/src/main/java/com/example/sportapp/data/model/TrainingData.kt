package com.example.sportapp.data.model

import java.util.Date

data class StartTrainingRequest(
    val user_id: Int,
    val training_type: String
)

data class CalculateFtpVo2maxRequest(
    val session_id: String
)

data class StartTrainingResponse (
    val session_id: String
)

data class StopTrainingRequest(
    val session_id: String,
    val end_time: Date,
    val duration: Int,
    val calories_burned: Int,
    val notes: String
)

data class StopTrainingResponse (
    val message: String,
    val session_id: String
)


data class ReceiveSesionDataRequest(
    val session_id: String,
    val power_output: Int,
    val max_heart_rate: Int,
    val resting_heart_rate: Int
)

data class ReceiveSesionDataResponse (
    val message: String
)
