// Generated by gencpp from file gazebo_launch/DriveForwardGoal.msg
// DO NOT EDIT!


#ifndef GAZEBO_LAUNCH_MESSAGE_DRIVEFORWARDGOAL_H
#define GAZEBO_LAUNCH_MESSAGE_DRIVEFORWARDGOAL_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace gazebo_launch
{
template <class ContainerAllocator>
struct DriveForwardGoal_
{
  typedef DriveForwardGoal_<ContainerAllocator> Type;

  DriveForwardGoal_()
    : speed(0)  {
    }
  DriveForwardGoal_(const ContainerAllocator& _alloc)
    : speed(0)  {
  (void)_alloc;
    }



   typedef int64_t _speed_type;
  _speed_type speed;





  typedef boost::shared_ptr< ::gazebo_launch::DriveForwardGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::gazebo_launch::DriveForwardGoal_<ContainerAllocator> const> ConstPtr;

}; // struct DriveForwardGoal_

typedef ::gazebo_launch::DriveForwardGoal_<std::allocator<void> > DriveForwardGoal;

typedef boost::shared_ptr< ::gazebo_launch::DriveForwardGoal > DriveForwardGoalPtr;
typedef boost::shared_ptr< ::gazebo_launch::DriveForwardGoal const> DriveForwardGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::gazebo_launch::DriveForwardGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::gazebo_launch::DriveForwardGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::gazebo_launch::DriveForwardGoal_<ContainerAllocator1> & lhs, const ::gazebo_launch::DriveForwardGoal_<ContainerAllocator2> & rhs)
{
  return lhs.speed == rhs.speed;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::gazebo_launch::DriveForwardGoal_<ContainerAllocator1> & lhs, const ::gazebo_launch::DriveForwardGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace gazebo_launch

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::gazebo_launch::DriveForwardGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::gazebo_launch::DriveForwardGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::gazebo_launch::DriveForwardGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::gazebo_launch::DriveForwardGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::gazebo_launch::DriveForwardGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::gazebo_launch::DriveForwardGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::gazebo_launch::DriveForwardGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4734ede392d478601ffe9898680ff4b5";
  }

  static const char* value(const ::gazebo_launch::DriveForwardGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4734ede392d47860ULL;
  static const uint64_t static_value2 = 0x1ffe9898680ff4b5ULL;
};

template<class ContainerAllocator>
struct DataType< ::gazebo_launch::DriveForwardGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "gazebo_launch/DriveForwardGoal";
  }

  static const char* value(const ::gazebo_launch::DriveForwardGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::gazebo_launch::DriveForwardGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#goal         \n"
"int64 speed\n"
;
  }

  static const char* value(const ::gazebo_launch::DriveForwardGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::gazebo_launch::DriveForwardGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.speed);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct DriveForwardGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::gazebo_launch::DriveForwardGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::gazebo_launch::DriveForwardGoal_<ContainerAllocator>& v)
  {
    s << indent << "speed: ";
    Printer<int64_t>::stream(s, indent + "  ", v.speed);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GAZEBO_LAUNCH_MESSAGE_DRIVEFORWARDGOAL_H
