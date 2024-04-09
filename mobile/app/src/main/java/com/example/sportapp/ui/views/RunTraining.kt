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

    private lateinit var chronometer: Chronometer
    private lateinit var startButton: Button
    private var isChronometerRunning: Boolean = false



    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_run_training)

        val tvwTypeRun = findViewById<TextView>(R.id.tvwTypeRun)
        val btnHome = findViewById<ImageView>(R.id.ivHome)

        btnHome.setOnClickListener{
            val home = Intent(this, Home::class.java)
            startActivity(home)
        }

        val valorRecibido = intent.getStringExtra("training")

        tvwTypeRun.text = getString(R.string.type_training)  + " " + valorRecibido

        chronometer = findViewById(R.id.chronometer)
        startButton = findViewById(R.id.btnStart)

        startButton.setOnClickListener { startChronometer(it) }
    }

    fun startChronometer(view: View) {
        if (!isChronometerRunning) {
            // Hacer visible el cronómetro y comenzar a contar
            chronometer.visibility = View.VISIBLE
            chronometer.base = SystemClock.elapsedRealtime()
            chronometer.start()

            // Cambiar el texto del botón a "Detener"
            startButton.text = getString(R.string.stop_training)
            isChronometerRunning = true
        } else {
            // Detener el cronómetro
            chronometer.stop()
            chronometer.pause()

            // Cambiar el texto del botón a "Iniciar"
            startButton.text = getString(R.string.start_training)
            isChronometerRunning = false
        }
    }
}
