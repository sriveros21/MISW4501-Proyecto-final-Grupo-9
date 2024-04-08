package com.example.sportapp.ui.views

import android.os.Bundle
import android.os.SystemClock
import android.view.View
import android.widget.Button
import android.widget.Chronometer
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.sportapp.R

class RunTraining : AppCompatActivity() {

    private lateinit var chronometer: Chronometer
    private lateinit var startButton: Button
    private var isChronometerRunning: Boolean = false
    val tvwTypeRun = findViewById<TextView>(R.id.tvwTypeRun)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_start_training)

        val valorRecibido = intent.getStringExtra("training")

        tvwTypeRun.text = getString(R.string.type_training)  + " " + valorRecibido

        chronometer = findViewById(R.id.chronometer)
        startButton = findViewById(R.id.btnStartTraining)

        // Asignar el método startChronometer al evento onClick del botón
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

            // Cambiar el texto del botón a "Iniciar"
            startButton.text = getString(R.string.start_training)
            isChronometerRunning = false
        }
    }
}
