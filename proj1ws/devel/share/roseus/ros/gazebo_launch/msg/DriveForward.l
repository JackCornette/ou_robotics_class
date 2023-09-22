;; Auto-generated. Do not edit!


(when (boundp 'gazebo_launch::DriveForward)
  (if (not (find-package "GAZEBO_LAUNCH"))
    (make-package "GAZEBO_LAUNCH"))
  (shadow 'DriveForward (find-package "GAZEBO_LAUNCH")))
(unless (find-package "GAZEBO_LAUNCH::DRIVEFORWARD")
  (make-package "GAZEBO_LAUNCH::DRIVEFORWARD"))

(in-package "ROS")
;;//! \htmlinclude DriveForward.msg.html


(defclass gazebo_launch::DriveForward
  :super ros::object
  :slots (_distance ))

(defmethod gazebo_launch::DriveForward
  (:init
   (&key
    ((:distance __distance) 0.0)
    )
   (send-super :init)
   (setq _distance (float __distance))
   self)
  (:distance
   (&optional __distance)
   (if __distance (setq _distance __distance)) _distance)
  (:serialization-length
   ()
   (+
    ;; float32 _distance
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _distance
       (sys::poke _distance (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _distance
     (setq _distance (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get gazebo_launch::DriveForward :md5sum-) "6e77fb10f0c8b4833ec273aa9ac74459")
(setf (get gazebo_launch::DriveForward :datatype-) "gazebo_launch/DriveForward")
(setf (get gazebo_launch::DriveForward :definition-)
      "# Custom message for driving forward
float32 distance    # Distance to drive forward (in meters)


")



(provide :gazebo_launch/DriveForward "6e77fb10f0c8b4833ec273aa9ac74459")


