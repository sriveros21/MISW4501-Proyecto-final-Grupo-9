package com.example.sportapp.ui.views

import android.content.Intent
import android.os.Bundle
import android.os.SystemClock
import android.view.View
import android.widget.Button
import android.widget.Chronometer
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.example.sportapp.R
import com.example.sportapp.ui.home.Home

class RunTraining : AppCompatActivity() {

    private lateinit var chronometer1: Chronometer
    private lateinit var startButton: Button
    private var isChronometerRunning: Boolean = false
    private var valorTraining: Int = 0
    private var typeTraining: String = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_run_training)

        val tvwTypeRun = findViewById<TextView>(R.id.tvwTypeRun)
        val btnHome = findViewById<ImageView>(R.id.ivHome)

        btnHome.setOnClickListener{
            val home = Intent(this, Home::class.java)
            startActivity(home)
        }


        typeTraining = intent.getStringExtra("training").toString()

        tvwTypeRun.text = getString(R.string.type_training)  + " " + typeTraining
        chronometer1 = findViewById(R.id.chronometer1)
        startButton = findViewById(R.id.btnStart)

        startButton.setOnClickListener { startChronometer() }

        startChronometer()
    }



    fun startChronometer() {
        if (!isChronometerRunning) {
            // Hacer visible el cronómetro y comenzar a contar
            chronometer1.visibility = View.VISIBLE
            //chronometer.format = "HH:mm:ss"
            chronometer1.base = SystemClock.elapsedRealtime()
            chronometer1.start()

            // Cambiar el texto del botón a "Detener"
            startButton.text = getString(R.string.stop_training)
            isChronometerRunning = true
        } else {
            // Detener el cronómetro
            chronometer1.stop()
            val tiempoDetenido = chronometer1.text.toString()
            val partesTiempo = tiempoDetenido.split(":")
            val minutos = partesTiempo[0].toInt()
            startButton.text = getString(R.string.start_training)
            isChronometerRunning = false

            //LLamar la nueva vista y pasar los parametros.
            finishTrainingActivity(minutos)

        }
    }

    private fun finishTrainingActivity(tiempoEjercicio: Int) {
        val finishTra = Intent(this, FinishTraining::class.java)
        var min = tiempoEjercicio
        if (min <= 0){
            min = 1
        }
        finishTra.putExtra("timeTraining", min)
        finishTra.putExtra("typeTraining", typeTraining)
        startActivity(finishTra)
    }
}
